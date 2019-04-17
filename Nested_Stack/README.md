This example contains code for deploying a nested stack. I've included sub-stacks that have exported variables which are then used in the other stacks. 

Note: I initially had a hard time piecing out this information from AWS official documentation, but the way to sequence these nested stacks is to use the 'DependsOn' tag
