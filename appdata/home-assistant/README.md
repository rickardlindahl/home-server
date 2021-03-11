# Home Assistant configuration files

This `home-assistant` configuration folder contains a `.gitignore` 
that hides the following files either because they contain 
details that are specific to an environment 
or because they contain secret credentials. 

## secrets.yaml

This is the Home Assistant configuration file that keeps private elements out of files that might be posted publicly, e.g. for troubleshooting

## Other files

* log files
	* home-assistant_v2.db*
	* home-assistant.log
* version and identity
	* .uuid
	* .HA_VERSION
* various registry files
	* .storage
* any certificates for https etc
	* *.cer
	* *.key

## Back up your files

As mentioned, git will ignore these file, 
so if you use a repo to store your config, 
then keep a backup copy of these file somewhere safe, especially:

* secrets.yaml
* .storage

If you loose `.storage` then you will loose 
all of your device registrations and customisations

