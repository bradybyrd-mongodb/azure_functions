# ----------------------------------------------------------------- #
#   Azure Function Setup
# ----------------------------------------------------------------- #
#  11/22/23 BJB

install azure core tools
install azurite
    npm install -g azurite
    /opt/homebrew/bin/azurite
    Start:
    https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite?tabs=npm
        azurite --silent --location /Users/brady.byrd/Documents/mongodb/dev/learning/azure_functions/blobstorage --debug /Users/brady.byrd/Documents/mongodb/dev/learning/azure_functions/blobstorage/debug.log

local lib install:
    pip3 install -r requirements.txt -t "/Users/brady.byrd/Documents/mongodb/dev/learning/azure_functions/lib"