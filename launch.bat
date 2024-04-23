@echo off
REM Setting up environment variables for USD Asset Resolver
set USD_ASSET_RESOLVER=C:/projects/UsdAssetResolver_v0.6.6
echo Using USD Asset Resolver from %USD_ASSET_RESOLVER%

REM Setting additional debugging and paths
set TF_DEBUG=AR_RESOLVER_INIT
set PATH=%USD_ASSET_RESOLVER%/cachedResolver/lib;%PATH%
set PXR_PLUGINPATH_NAME=%USD_ASSET_RESOLVER%/cachedResolver/resources;%PXR_PLUGINPATH_NAME%
set PYTHONPATH=%USD_ASSET_RESOLVER%/cachedResolver/lib/python;%PYTHONPATH%

REM Launch Houdini
echo Launching Houdini...
C:/PROGRA~1/SIDEEF~1/HOUDIN~1.653/bin/houdini
 