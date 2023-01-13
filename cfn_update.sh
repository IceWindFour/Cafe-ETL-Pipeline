#!/bin/bash

# Get the file name and stack name
file=$1
stack_name=$2

# Get the hashes of the files
hash1=$(md5sum $file | awk '{print $1}')
hash2=$(aws cloudformation describe-stacks --stack-name $stack_name --query "Stacks[0].TemplateBody" | md5sum | awk '{print $1}')

# Compare the hashes
if [ "$hash1" != "$hash2" ]; then
    echo "The files are different, updating the stack..."
    aws cloudformation update-stack --stack-name $stack_name --template-body file://$file
else
    echo "The files are identical, no update needed."
fi