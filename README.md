# Web Scraper using Vagrant with Selenium
Vagrant configuration base on ubuntu/trusty64, ready to be used with Selenium and Python

## Introduction

Selenium allows you to automate tests in Web Browsers.

## Installation

1. Install [Vagrant](https://www.vagrantup.com)
2. Clone this git repository
3. Run the command `vagrant up`

This vagrant works for *Virtualbox*, on a 64 bits machine.

## Browser support

- Firefox (latest version)

The script also installs the latest version of selenium server, and google chrome webdriver.

## Why a VM for Selenium?

Installing selenium server and the webdrivers are easy on a machine. However, everytime that you want to run your tests, it opens the browser on top of the other windows, preventing you from doing something else. Unless you use phantomjs, it is not possible to run Chrome or Firefox hidden, without disturbing you on your work.

Thanks to this VM, you only need to start the VM, and all your tests will be run into the VM. You can continue developping in the meanwhile!

## How does it work?

After installing the VM via Vagrant you need to restart it by running the command 'vagrant halt' and after that 'vagrant up', this is necessary to sync the folder inluding the vagrantfile with the folder '/vagrant' on the virtual machine.

To connect to the VM Shell run 'vagrant ssh'

Move to your synced folder by running 'cd /vagrant', here you will find the Scripts you dropped to the Folder that is including the vagrantfile.

To start your script run 'xvfb-run python yourscript.py'
