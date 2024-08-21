#!/bin/bash

# for installing specific version of Python
# written by Ye Kyaw Thu, LU Lab., Myanmar
# last updated: 21 Aug 2024
# Note: you need sudo right
# ref: https://www.python.org/downloads/

# Function to display usage
usage() {
    echo "Usage: $0 [-v <python_version>] [-i version-info]"
    echo "  -v <python_version>  Specify the Python version to install."
    echo "  -i version-info      Display available Python versions."
    exit 1
}

# Function to display Python version information
version_info() {
    echo "Available Python versions:"
    echo "Python 3.12.5 Aug. 6, 2024"
    echo "Python 3.12.4 June 6, 2024"
    echo "Python 3.12.3 April 9, 2024"
    echo "Python 3.11.9 April 2, 2024"
    echo "Python 3.10.14 March 19, 2024"
    echo "Python 3.9.19 March 19, 2024"
    echo "Python 3.8.19 March 19, 2024"
    echo "Python 3.11.8 Feb. 6, 2024"
    echo "Python 3.12.2 Feb. 6, 2024"
    echo "Python 3.12.1 Dec. 8, 2023"
    echo "Python 3.11.7 Dec. 4, 2023"
    echo "Python 3.12.0 Oct. 2, 2023"
    echo "Python 3.11.6 Oct. 2, 2023"
    echo "Python 3.11.5 Aug. 24, 2023"
    echo "Python 3.10.13 Aug. 24, 2023"
    echo "Python 3.9.18 Aug. 24, 2023"
    echo "Python 3.8.18 Aug. 24, 2023"
    echo "Python 3.10.12 June 6, 2023"
    echo "Python 3.11.4 June 6, 2023"
    echo "Python 3.7.17 June 6, 2023"
    echo "Python 3.8.17 June 6, 2023"
    echo "Python 3.9.17 June 6, 2023"
    echo "Python 3.10.11 April 5, 2023"
    echo "Python 3.11.3 April 5, 2023"
    echo "Python 3.10.10 Feb. 8, 2023"
    echo "Python 3.11.2 Feb. 8, 2023"
    echo "Python 3.11.1 Dec. 6, 2022"
    echo "Python 3.10.9 Dec. 6, 2022"
    echo "Python 3.9.16 Dec. 6, 2022"
    echo "Python 3.8.16 Dec. 6, 2022"
    echo "Python 3.7.16 Dec. 6, 2022"
    echo "Python 3.11.0 Oct. 24, 2022"
    echo "Python 3.9.15 Oct. 11, 2022"
    echo "Python 3.8.15 Oct. 11, 2022"
    echo "Python 3.10.8 Oct. 11, 2022"
    echo "Python 3.7.15 Oct. 11, 2022"
    echo "Python 3.7.14 Sept. 6, 2022"
    echo "Python 3.8.14 Sept. 6, 2022"
    echo "Python 3.9.14 Sept. 6, 2022"
    echo "Python 3.10.7 Sept. 6, 2022"
    echo "Python 3.10.6 Aug. 2, 2022"
    echo "Python 3.10.5 June 6, 2022"
    echo "Python 3.9.13 May 17, 2022"
    echo "Python 3.10.4 March 24, 2022"
    echo "Python 3.9.12 March 23, 2022"
    echo "Python 3.10.3 March 16, 2022"
    echo "Python 3.9.11 March 16, 2022"
    echo "Python 3.8.13 March 16, 2022"
    echo "Python 3.7.13 March 16, 2022"
    echo "Python 3.9.10 Jan. 14, 2022"
    echo "Python 3.10.2 Jan. 14, 2022"
    echo "Python 3.10.1 Dec. 6, 2021"
    echo "Python 3.9.9 Nov. 15, 2021"
    echo "Python 3.9.8 Nov. 5, 2021"
    echo "Python 3.10.0 Oct. 4, 2021"
    echo "Python 3.7.12 Sept. 4, 2021"
    echo "Python 3.6.15 Sept. 4, 2021"
    echo "Python 3.9.7 Aug. 30, 2021"
    echo "Python 3.8.12 Aug. 30, 2021"
    echo "Python 3.9.6 June 28, 2021"
    echo "Python 3.8.11 June 28, 2021"
    echo "Python 3.6.14 June 28, 2021"
    echo "Python 3.7.11 June 28, 2021"
    echo "Python 3.9.5 May 3, 2021"
    echo "Python 3.8.10 May 3, 2021"
    echo "Python 3.9.4 April 4, 2021"
    echo "Python 3.8.9 April 2, 2021"
    echo "Python 3.9.2 Feb. 19, 2021"
    echo "Python 3.8.8 Feb. 19, 2021"
    echo "Python 3.6.13 Feb. 15, 2021"
    echo "Python 3.7.10 Feb. 15, 2021"
    echo "Python 3.8.7 Dec. 21, 2020"
    echo "Python 3.9.1 Dec. 7, 2020"
    echo "Python 3.9.0 Oct. 5, 2020"
    echo "Python 3.8.6 Sept. 24, 2020"
    echo "Python 3.5.10 Sept. 5, 2020"
    echo "Python 3.7.9 Aug. 17, 2020"
    echo "Python 3.6.12 Aug. 17, 2020"
    echo "Python 3.8.5 July 20, 2020"
    echo "Python 3.8.4 July 13, 2020"
    echo "Python 3.7.8 June 27, 2020"
    echo "Python 3.6.11 June 27, 2020"
    echo "Python 3.8.3 May 13, 2020"
    echo "Python 2.7.18 April 20, 2020"
    echo "Python 3.7.7 March 10, 2020"
    echo "Python 3.8.2 Feb. 24, 2020"
    echo "Python 3.8.1 Dec. 18, 2019"
    echo "Python 3.7.6 Dec. 18, 2019"
    echo "Python 3.6.10 Dec. 18, 2019"
    echo "Python 3.5.9 Nov. 2, 2019"
    echo "Python 3.5.8 Oct. 29, 2019"
    echo "Python 2.7.17 Oct. 19, 2019"
    echo "Python 3.7.5 Oct. 15, 2019"
    echo "Python 3.8.0 Oct. 14, 2019"
    echo "Python 3.7.4 July 8, 2019"
    echo "Python 3.6.9 July 2, 2019"
    echo "Python 3.7.3 March 25, 2019"
    echo "Python 3.4.10 March 18, 2019"
    echo "Python 3.5.7 March 18, 2019"
    echo "Python 2.7.16 March 4, 2019"
    echo "Python 3.7.2 Dec. 24, 2018"
    echo "Python 3.6.8 Dec. 24, 2018"
    echo "Python 3.7.1 Oct. 20, 2018"
    echo "Python 3.6.7 Oct. 20, 2018"
    echo "Python 3.5.6 Aug. 2, 2018"
    echo "Python 3.4.9 Aug. 2, 2018"
    echo "Python 3.7.0 June 27, 2018"
    echo "Python 3.6.6 June 27, 2018"
    echo "Python 2.7.15 May 1, 2018"
    echo "Python 3.6.5 March 28, 2018"
    echo "Python 3.4.8 Feb. 5, 2018"
    echo "Python 3.5.5 Feb. 5, 2018"
    echo "Python 3.6.4 Dec. 19, 2017"
    echo "Python 3.6.3 Oct. 3, 2017"
    echo "Python 3.3.7 Sept. 19, 2017"
    echo "Python 2.7.14 Sept. 16, 2017"
    echo "Python 3.4.7 Aug. 9, 2017"
    echo "Python 3.5.4 Aug. 8, 2017"
    echo "Python 3.6.2 July 17, 2017"
    echo "Python 3.6.1 March 21, 2017"
    echo "Python 3.4.6 Jan. 17, 2017"
    echo "Python 3.5.3 Jan. 17, 2017"
    echo "Python 3.6.0 Dec. 23, 2016"
    echo "Python 2.7.13 Dec. 17, 2016"
    echo "Python 3.4.5 June 27, 2016"
    echo "Python 3.5.2 June 27, 2016"
    echo "Python 2.7.12 June 25, 2016"
    echo "Python 3.4.4 Dec. 21, 2015"
    echo "Python 3.5.1 Dec. 7, 2015"
    echo "Python 2.7.11 Dec. 5, 2015"
    echo "Python 3.5.0 Sept. 13, 2015"
    echo "Python 2.7.10 May 23, 2015"
    echo "Python 3.4.3 Feb. 25, 2015"
    echo "Python 2.7.9 Dec. 10, 2014"
    echo "Python 3.4.2 Oct. 13, 2014"
    echo "Python 3.3.6 Oct. 12, 2014"
    echo "Python 3.2.6 Oct. 12, 2014"
    echo "Python 2.7.8 July 2, 2014"
    echo "Python 2.7.7 June 1, 2014"
    echo "Python 3.4.1 May 19, 2014"
    echo "Python 3.4.0 March 17, 2014"
    echo "Python 3.3.5 March 9, 2014"
    echo "Python 3.3.4 Feb. 9, 2014"
    echo "Python 3.3.3 Nov. 17, 2013"
    echo "Python 2.7.6 Nov. 10, 2013"
    echo "Python 2.6.9 Oct. 29, 2013"
    echo "Python 3.3.2 May 15, 2013"
    echo "Python 3.2.5 May 15, 2013"
    echo "Python 2.7.5 May 12, 2013"
    echo "Python 2.7.4 April 6, 2013"
    echo "Python 3.2.4 April 6, 2013"
    echo "Python 3.3.1 April 6, 2013"
    echo "Python 3.3.0 Sept. 29, 2012"
    echo "Python 3.2.3 April 10, 2012"
    echo "Python 2.6.8 April 10, 2012"
    echo "Python 3.1.5 April 9, 2012"
    echo "Python 2.7.3 April 9, 2012"
    echo "Python 3.2.2 Sept. 3, 2011"
    echo "Python 3.2.1 July 9, 2011"
    echo "Python 2.7.2 June 11, 2011"
    echo "Python 3.1.4 June 11, 2011"
    echo "Python 2.6.7 June 3, 2011"
    echo "Python 2.5.6 May 26, 2011"
    echo "Python 3.2.0 Feb. 20, 2011"
    echo "Python 3.1.3 Nov. 27, 2010"
    echo "Python 2.7.1 Nov. 27, 2010"
    echo "Python 2.6.6 Aug. 24, 2010"
    echo "Python 2.7.0 July 3, 2010"
    echo "Python 3.1.2 March 20, 2010"
    echo "Python 2.6.5 March 18, 2010"
    echo "Python 2.5.5 Jan. 31, 2010"
    echo "Python 2.6.4 Oct. 26, 2009"
    echo "Python 2.6.3 Oct. 2, 2009"
    echo "Python 3.1.1 Aug. 17, 2009"
    echo "Python 3.1.0 June 26, 2009"
    echo "Python 2.6.2 April 14, 2009"
    echo "Python 3.0.1 Feb. 13, 2009"
    echo "Python 2.5.4 Dec. 23, 2008"
    echo "Python 2.4.6 Dec. 19, 2008"
    echo "Python 2.5.3 Dec. 19, 2008"
    echo "Python 2.6.1 Dec. 4, 2008"
    echo "Python 3.0.0 Dec. 3, 2008"
    echo "Python 2.6.0 Oct. 2, 2008"
    echo "Python 2.3.7 March 11, 2008"
    echo "Python 2.4.5 March 11, 2008"
    echo "Python 2.5.2 Feb. 21, 2008"
    echo "Python 2.5.1 April 19, 2007"
    echo "Python 2.3.6 Nov. 1, 2006"
    echo "Python 2.4.4 Oct. 18, 2006"
    echo "Python 2.5.0 Sept. 19, 2006"
    echo "Python 2.4.3 April 15, 2006"
    echo "Python 2.4.2 Sept. 27, 2005"
    echo "Python 2.4.1 March 30, 2005"
    echo "Python 2.3.5 Feb. 8, 2005"
    echo "Python 2.4.0 Nov. 30, 2004"
    echo "Python 2.3.4 May 27, 2004"
    echo "Python 2.3.3 Dec. 19, 2003"
    echo "Python 2.3.2 Oct. 3, 2003"
    echo "Python 2.3.1 Sept. 23, 2003"
    echo "Python 2.3.0 July 29, 2003"
    echo "Python 2.2.3 May 30, 2003"
    echo "Python 2.2.2 Oct. 14, 2002"
    echo "Python 2.2.1 April 10, 2002"
    echo "Python 2.1.3 April 9, 2002"
    echo "Python 2.2.0 Dec. 21, 2001"
    echo "Python 2.0.1 June 22, 2001"
    exit 0
}

# Check if the user passed arguments
if [ $# -eq 0 ]; then
    usage
fi

# Parse command-line arguments
while getopts ":v:i" opt; do
    case $opt in
        v)
            PYTHON_VERSION=$OPTARG
            ;;
        i)
            version_info
            ;;
        *)
            usage
            ;;
    esac
done

# Exit if no Python version is specified
if [ -z "$PYTHON_VERSION" ]; then
    usage
fi

# Define download URL and file names
URL="https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz"
FILE="Python-$PYTHON_VERSION.tgz"
DIR="Python-$PYTHON_VERSION"

# Navigate to /tmp directory
cd /tmp || { echo "Failed to change directory to /tmp"; exit 1; }

# Download the specified Python version
echo "Downloading Python $PYTHON_VERSION..."
wget $URL || { echo "Failed to download Python $PYTHON_VERSION"; exit 1; }

# Extract the tarball
echo "Extracting $FILE..."
tar xzvf $FILE || { echo "Failed to extract $FILE"; exit 1; }

# Navigate to the extracted directory
cd $DIR || { echo "Failed to change directory to $DIR"; exit 1; }

# Configure, make, and install Python
echo "Configuring Python $PYTHON_VERSION..."
./configure || { echo "Failed to configure Python $PYTHON_VERSION"; exit 1; }

echo "Building Python $PYTHON_VERSION..."
make || { echo "Failed to build Python $PYTHON_VERSION"; exit 1; }

echo "Installing Python $PYTHON_VERSION..."
sudo make install || { echo "Failed to install Python $PYTHON_VERSION"; exit 1; }

echo "Python $PYTHON_VERSION installed successfully."
