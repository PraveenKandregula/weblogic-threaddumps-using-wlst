1. Place both the scripts in same directory.
2. This script will generate 6 threaddumps of all servers in a domain with the interval of 10 secs.
3. This script connects to admin server to generate threaddumps. Any issues with admin server connectivity might result runtime issues and no dumps.
4. Dumps will be genarted at same directory as scripts
5. More than one run per day result in vanishing of old dumps of same day.
6. Python script works on any OS. However sourcing setDomainEnv.sh and invoking python script can be modified per the OS.