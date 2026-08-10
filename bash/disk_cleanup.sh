#!/bin/bash
# disk_cleanup.sh - Comprehensive disk space cleanup tool
# Usage: ./disk_cleanup.sh [--dry-run] [--aggressive] [--help]

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
DRY_RUN=false
AGGRESSIVE=false
LOG_FILE="/tmp/disk_cleanup_$(date +%Y%m%d_%H%M%S).log"
SECONDARY_DISK="/mnt/disk1"
USER_HOME="${HOME}"

# Parse arguments
for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --aggressive)
            AGGRESSIVE=true
            shift
            ;;
        --help)
            echo "Usage: $0 [--dry-run] [--aggressive] [--help]"
            echo "  --dry-run     Show what would be cleaned without deleting"
            echo "  --aggressive  Perform aggressive cleanup (use with caution)"
            echo "  --help        Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $arg"
            exit 1
            ;;
    esac
done

# Logging function
log() {
    local level=$1
    local message=$2
    echo -e "${level}${message}${NC}" | tee -a "$LOG_FILE"
}

# Get disk usage percentage
get_disk_usage() {
    local partition=$1
    df -h "$partition" | awk 'NR==2 {print $5}' | tr -d '%'
}

# Get available space in GB
get_available_space() {
    local partition=$1
    df -BG "$partition" | awk 'NR==2 {print $4}' | tr -d 'G'
}

# Calculate directory size
get_dir_size() {
    local dir=$1
    du -sh "$dir" 2>/dev/null | awk '{print $1}'
}

# Check if running as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        log "$YELLOW" "⚠️  Not running as root. Some operations may fail."
        log "$YELLOW" "   Run with sudo for full cleanup capabilities."
    fi
}

# Clean pip cache
clean_pip_cache() {
    log "$BLUE" "🐍 Cleaning pip cache..."
    
    local pip_cache_dir
    pip_cache_dir=$(pip cache dir 2>/dev/null || echo "")
    
    if [ -n "$pip_cache_dir" ] && [ -d "$pip_cache_dir" ]; then
        local before_size
        before_size=$(get_dir_size "$pip_cache_dir")
        
        if [ "$DRY_RUN" = false ]; then
            pip cache purge > /dev/null 2>&1 || true
        fi
        
        log "$GREEN" "   ✓ Cleaned pip cache (was: $before_size)"
    else
        log "$YELLOW" "   ℹ️  No pip cache found"
    fi
}

# Clean Poetry cache
clean_poetry_cache() {
    log "$BLUE" "📦 Cleaning Poetry cache..."
    
    if command -v poetry &> /dev/null; then
        local poetry_cache_dir
        poetry_cache_dir=$(poetry config cache-dir 2>/dev/null || echo "")
        
        if [ -n "$poetry_cache_dir" ] && [ -d "$poetry_cache_dir" ]; then
            local before_size
            before_size=$(get_dir_size "$poetry_cache_dir")
            
            if [ "$DRY_RUN" = false ]; then
                poetry cache clear --all > /dev/null 2>&1 || true
            fi
            
            log "$GREEN" "   ✓ Cleaned Poetry cache (was: $before_size)"
        else
            log "$YELLOW" "   ℹ️  No Poetry cache found"
        fi
    else
        log "$YELLOW" "   ℹ️  Poetry not installed"
    fi
}

# Clean conda cache
clean_conda_cache() {
    log "$BLUE" "🐍 Cleaning conda cache..."
    
    if command -v conda &> /dev/null; then
        if [ "$DRY_RUN" = false ]; then
            conda clean --all -y > /dev/null 2>&1 || true
        fi
        log "$GREEN" "   ✓ Cleaned conda cache"
    else
        log "$YELLOW" "   ℹ️  Conda not installed"
    fi
}

# Clean apt cache
clean_apt_cache() {
    log "$BLUE" "📦 Cleaning apt cache..."
    
    if [ "$DRY_RUN" = false ]; then
        sudo apt-get clean > /dev/null 2>&1 || true
        sudo apt-get autoclean > /dev/null 2>&1 || true
        sudo apt-get autoremove -y > /dev/null 2>&1 || true
    fi
    
    local apt_cache_size
    apt_cache_size=$(sudo du -sh /var/cache/apt 2>/dev/null | awk '{print $1}')
    log "$GREEN" "   ✓ Cleaned apt cache (current size: $apt_cache_size)"
}

# Clean journal logs
clean_journal_logs() {
    log "$BLUE" "📝 Cleaning journal logs..."
    
    local before_size
    before_size=$(sudo du -sh /var/log/journal 2>/dev/null | awk '{print $1}')
    
    if [ "$DRY_RUN" = false ]; then
        sudo journalctl --vacuum-time=2d > /dev/null 2>&1 || true
        sudo journalctl --vacuum-size=100M > /dev/null 2>&1 || true
    fi
    
    local after_size
    after_size=$(sudo du -sh /var/log/journal 2>/dev/null | awk '{print $1}')
    log "$GREEN" "   ✓ Cleaned journal logs (before: $before_size, after: $after_size)"
}

# Clean old log files
clean_old_logs() {
    log "$BLUE" "🗑️  Cleaning old log files..."
    
    local log_files_count
    log_files_count=$(sudo find /var/log -type f -name "*.log" -mtime +30 2>/dev/null | wc -l)
    
    if [ "$log_files_count" -gt 0 ]; then
        if [ "$DRY_RUN" = false ]; then
            sudo find /var/log -type f -name "*.log" -mtime +30 -exec rm -f {} \; 2>/dev/null || true
            sudo find /var/log -type f -name "*.log.*" -mtime +30 -exec rm -f {} \; 2>/dev/null || true
        fi
        log "$GREEN" "   ✓ Removed $log_files_count old log files"
    else
        log "$YELLOW" "   ℹ️  No old log files found"
    fi
}

# Clean temporary files
clean_temp_files() {
    log "$BLUE" "🧹 Cleaning temporary files..."
    
    local tmp_size
    tmp_size=$(sudo du -sh /tmp 2>/dev/null | awk '{print $1}')
    
    if [ "$DRY_RUN" = false ]; then
        sudo rm -rf /tmp/* /var/tmp/* 2>/dev/null || true
    fi
    
    log "$GREEN" "   ✓ Cleaned /tmp and /var/tmp (was: $tmp_size)"
}

# Clean Docker resources
clean_docker() {
    log "$BLUE" "🐳 Cleaning Docker resources..."
    
    if command -v docker &> /dev/null; then
        if [ "$DRY_RUN" = false ]; then
            docker system prune -af --volumes > /dev/null 2>&1 || true
        fi
        log "$GREEN" "   ✓ Cleaned Docker images, containers, and volumes"
    else
        log "$YELLOW" "   ℹ️  Docker not installed"
    fi
}

# Find large files
find_large_files() {
    log "$BLUE" "🔍 Finding large files (>100MB)..."
    
    echo -e "\n${BLUE}Large files in home directory (>100MB):${NC}" | tee -a "$LOG_FILE"
    find "$USER_HOME" -type f -size +100M -exec ls -lh {} \; 2>/dev/null | \
        awk '{print $5, $9}' | sort -rh | head -20 | tee -a "$LOG_FILE"
    
    if [ "$AGGRESSIVE" = true ]; then
        echo -e "\n${BLUE}Large files system-wide (>500MB):${NC}" | tee -a "$LOG_FILE"
        sudo find / -type f -size +500M 2>/dev/null | \
            xargs sudo ls -lhS 2>/dev/null | head -20 | tee -a "$LOG_FILE"
    fi
}

# Find large directories
find_large_dirs() {
    log "$BLUE" "📁 Finding large directories..."
    
    echo -e "\n${BLUE}Top 20 largest directories in home:${NC}" | tee -a "$LOG_FILE"
    du -sh "$USER_HOME"/* 2>/dev/null | sort -rh | head -20 | tee -a "$LOG_FILE"
    
    echo -e "\n${BLUE}Top 20 largest directories in /var:${NC}" | tee -a "$LOG_FILE"
    sudo du -sh /var/* 2>/dev/null | sort -rh | head -20 | tee -a "$LOG_FILE"
}

# Move caches to secondary disk
move_caches_to_secondary() {
    if [ ! -d "$SECONDARY_DISK" ]; then
        log "$YELLOW" "⚠️  Secondary disk $SECONDARY_DISK not found"
        return
    fi
    
    log "$BLUE" "💾 Moving caches to secondary disk..."
    
    # Create cache directory on secondary disk
    local secondary_cache_dir="${SECONDARY_DISK}/ye/.cache"
    mkdir -p "$secondary_cache_dir"
    
    # Move pip cache
    if [ -d "$USER_HOME/.cache/pip" ]; then
        local pip_size
        pip_size=$(get_dir_size "$USER_HOME/.cache/pip")
        
        if [ "$DRY_RUN" = false ]; then
            mv "$USER_HOME/.cache/pip" "$secondary_cache_dir/pip"
            ln -s "$secondary_cache_dir/pip" "$USER_HOME/.cache/pip"
        fi
        
        log "$GREEN" "   ✓ Moved pip cache to secondary disk (size: $pip_size)"
    fi
    
    # Move poetry cache if exists
    if [ -d "$USER_HOME/.cache/pypoetry" ]; then
        local poetry_size
        poetry_size=$(get_dir_size "$USER_HOME/.cache/pypoetry")
        
        if [ "$DRY_RUN" = false ]; then
            mv "$USER_HOME/.cache/pypoetry" "$secondary_cache_dir/pypoetry"
            ln -s "$secondary_cache_dir/pypoetry" "$USER_HOME/.cache/pypoetry"
        fi
        
        log "$GREEN" "   ✓ Moved Poetry cache to secondary disk (size: $poetry_size)"
    fi
}

# Display disk usage summary
show_disk_summary() {
    log "$BLUE" "📊 Disk Usage Summary:"
    echo
    df -h | grep -vE "^Filesystem|tmpfs|cdrom" | tee -a "$LOG_FILE"
    echo
    
    local root_usage
    root_usage=$(get_disk_usage "/")
    local root_available
    root_available=$(get_available_space "/")
    
    if [ "$root_usage" -gt 90 ]; then
        log "$RED" "⚠️  Root partition is ${root_usage}% full (only ${root_available}GB available)"
    elif [ "$root_usage" -gt 80 ]; then
        log "$YELLOW" "⚠️  Root partition is ${root_usage}% full (${root_available}GB available)"
    else
        log "$GREEN" "✓ Root partition is ${root_usage}% full (${root_available}GB available)"
    fi
}

# Main cleanup function
main_cleanup() {
    log "$GREEN" "🚀 Starting disk cleanup..."
    log "$BLUE" "📋 Log file: $LOG_FILE"
    echo
    
    if [ "$DRY_RUN" = true ]; then
        log "$YELLOW" "🏃 DRY RUN MODE - No files will be deleted"
        echo
    fi
    
    # Check root privileges
    check_root
    
    # Show initial disk usage
    show_disk_summary
    echo
    
    # Clean various caches
    clean_pip_cache
    clean_poetry_cache
    clean_conda_cache
    clean_apt_cache
    clean_journal_logs
    clean_old_logs
    clean_temp_files
    
    # Aggressive cleanup
    if [ "$AGGRESSIVE" = true ]; then
        log "$YELLOW" "🔥 Aggressive cleanup mode enabled"
        clean_docker
        move_caches_to_secondary
    fi
    
    echo
    find_large_files
    echo
    find_large_dirs
    echo
    
    # Show final disk usage
    show_disk_summary
    
    log "$GREEN" "✅ Disk cleanup completed!"
    log "$BLUE" "📝 Full log saved to: $LOG_FILE"
    
    # Suggest next steps if still low on space
    local root_available
    root_available=$(get_available_space "/")
    
    if [ "$root_available" -lt 10 ]; then
        echo
        log "$RED" "❗ Still low on disk space. Consider:"
        log "$YELLOW" "   - Moving large files to $SECONDARY_DISK"
        log "$YELLOW" "   - Removing unused conda environments: 'conda env list'"
        log "$YELLOW" "   - Cleaning Docker images: 'docker system prune -a'"
        log "$YELLOW" "   - Removing old project files"
        log "$YELLOW" "   - Running with --aggressive flag"
    fi
}

# Run main function
main_cleanup

