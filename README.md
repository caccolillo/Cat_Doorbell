# Cat_Doorbell
In this repo, there's the full project about a vision based cat doorbell, leveraging upon CNNs.

To clone it:

Shallow Clone

First, turn off compression:

git config --global core.compression 0

Next, let's do a partial clone to truncate the amount of info coming down:

git clone --depth 1 <repo_URI>

When that works, go into the new directory and retrieve the rest of the clone:

git fetch --unshallow

or, alternately,

git fetch --depth=2147483647

Now, do a pull:

git pull --all

