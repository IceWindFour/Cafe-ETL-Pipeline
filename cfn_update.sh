#!/bin/bash

# Get the file name and stack name
cloudformation_file=$1

hash_file="$(<$2)"

echo $hash_file
value="$(cat $hash_file)" 
working_dir=$3


# Get the hashes of the files
hash1=$(md5sum $file | awk '{print $1}')
hash2=$(echo "$value" | awk '{print $1;}')


# Compare the hashes
if [ "$hash1" != "$hash2" ]; then
    echo "The files are different, updating the stack..."
    # aws cloudformation update-stack --stack-name $stack_name --template-body file://$file

    # upload the updated hash into a txt in oldmengrinding bucket
    hash1 > working_dir/hash.txt
    # update the stack
    exit 1
else
    echo "The files are identical, no update needed."
    exit 0
fi