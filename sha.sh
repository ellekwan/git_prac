#!/bin/bash

#FUNCTIONS TOC:
#DEF_HASH 	= define hash type
#SUMSG		= check signature file sums
#KEY_IMPORT	= import key file
#VER_SIG	= verify signature file
#VER		= gpg --verify
#SHA		= shasum txt

###################################################################
###___ FUNCTIONS___###

function DEF_HASH
{
until [[ "$reply" = "0" ]] || [[ "$reply" = "1" ]];
do

echo "
Select hash function by pressing either 0 or 1:

0)  SHA256
1)  md5

"
read reply
case $reply in

0) sum_typ="sha256"
echo " >>   hash is SHA256.
"
break;;


1) sum_typ="md5"
echo " >>   hash is md5.
"
break;;


q) exit;;


*)  echo "xx >   please enter either 0 or 1, or Ctrl+C to quit.";
sleep 2; clear;;

esac
done
}

##########################################################################
function 256SUM
{
sha256sum -c $sigtxt
}

function md5SUM
{
md5sum -c $sigtxt
}

function SUMSG
{
#echo "
#Select signature.txt file to verify it:
#";
#select sigtxt in *;
#do
	
	sigtxt="$dname*.txt" 
        echo " 
Checking $sigtxt for verification...
";
        if sum_typ="sha256"; then
        
if 256SUM | grep "BAD"; then echo "
	Failed to verify, quitting." && exit 1
else 256SUM && echo "
	Signature verified.";
fi       	

        else 

if md5SUM | grep "BAD"; then echo "
	Failed to verify, quitting." && exit 1
else md5SUM && echo "
	Signature verified.";       
fi
        fi
#done
}


###########################################################################################

function gpg_imp
{
gpg --import $key
}
#check and import key file
function KEY_IMPORT
{
#echo "Select key file for import"
#select key in *.asc;
#do
 	key=*key.asc
     echo "
	Importing key file $key...
	"
if gpg_imp | grep "0"; then  echo "
	Key import failed, exiting.
	" && exit 1
else gpg_imp && echo "
	Key imported.
	";
fi
#done
}

###########################################################################################

function VER
{
gpg --verify *SUMS.sig* $sigtxt
}


#Verifying signature file

function VER_SIG
{
if [ -e *SUMS.sig ]; then
	echo "verifying signature file..." 
else 	echo "signature file not found. please download appropriate .sig file." && exit=1
fi

VER || echo "
FAILED, signature could not be verified.
==>> ...
==>> exiting program now...
"; exit 1

VER && echo "
Signature file verified
"; break


}

##############################################################################################

function SHA
{
 if [ sum_typ="sha256" ]; then
        echo "
        Verifying SHASUM...
        ";
        shasum -a 256 -c $sigtxt
        else exit

fi
}
##################################################

function NXT
{
sleep 0.5                                                                                           
}
####################################################################################################


###___SCRIPT BEGINS___###

clear
cd ~/Downloads
echo "
Enter download name:
	  {"
ls -lA
echo "		}  ==>"

#enter string in all associated filenames {downloaded pkg, keys, sig};
# e.g. vagrant,/ atom ,/ tor ,/ etc.

read dname

if [ ! -d ~/Downloads/dir_$dname ];
	then mkdir ~/Downloads/dir_$dname ; echo "Creating directory for package..."

fi

#create a directory for download
echo "moving downloaded files to the directory:  dir_$dname"
mv ~/Downloads/*$dname*.* ~/Downloads/dir_$dname
cd ~/Downloads/dir_$dname
clear

DEF_HASH;
clear; NXT;
SUMSG; NXT;

if [ ! -e *key.asc ]; then
 echo "no key file found."
else  KEY_IMPORT
fi

NXT;
VER_SIG; NXT;
SHA;

echo "

--_--_--_>>  Verification complete.  <<_--_--_--
"
exit
