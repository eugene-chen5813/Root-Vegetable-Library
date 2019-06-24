# -*- mode: ruby -*-
# vi: set ft=ruby :

# Here we create the variable `nodes`, where we define each server with its
# hostname and IP address.
nodes = [
  { :hostname => 'webserver1.test', :ip => '10.101.0.2' },
  { :hostname => 'webserver2.test', :ip => '10.101.0.3' },
  { :hostname => 'loadbalancer.test', :ip => '10.101.0.4' },
  { :hostname => 'database1.test', :ip => '10.101.0.5' },
  { :hostname => 'database2.test', :ip => '10.101.0.6' }
]


# Declare configuration version 2. See
# https://www.vagrantup.com/docs/vagrantfile/version.html.
Vagrant.configure("2") do |config|

  # Vagrant boxes allow anyone to package their environment into an image and
  # share it with others. See https://app.vagrantup.com/boxes/search.
  config.vm.box = "centos/7"

  # By default, Vagrant will share your project directory to `/vagrant` inside
  # the virtual machine. See https://www.vagrantup.com/docs/synced-folders/.
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider :virtualbox do |vb|
    vb.memory = 512
    vb.cpus = 1
  end

  # Here we loop through the variable `nodes`, deploying and provisioning each
  # of our servers.
  nodes.each do |node|
    config.vm.define node[:hostname] do |nodeconfig|
      nodeconfig.vm.hostname = node[:hostname]
      nodeconfig.vm.network "private_network", ip: node[:ip]
 
      # Vagrant supports a number of provisioners. Using the Ansible
      # provisioner, we can tell Vagrant to automatically run our playbooks
      # after a virtual machine is deployed.
      #
      # See https://www.vagrantup.com/docs/provisioning/ansible.html.
      nodeconfig.vm.provision :ansible do |ansible|
        ansible.playbook = "site.yml"
        ansible.inventory_path = "inventory/development"
      end
    end
  end
end
