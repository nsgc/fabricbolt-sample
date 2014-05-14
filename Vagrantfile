VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu13.10"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/saucy/current/saucy-server-cloudimg-i386-vagrant-disk1.box"

  config.vm.define "bolt" do |bolt|
    bolt.vm.network "private_network", ip: "192.168.111.221"
    bolt.vm.network "forwarded_port", guest: 8000, host: 8000

    bolt.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/provisioning/bolt.yml"
    end
  end

  config.vm.define "gw" do |gw|
    gw.vm.network "private_network", ip: "192.168.111.222"
  end

  config.vm.define "web" do |web|
    web.vm.network "private_network", ip: "192.168.111.223"
  end
end
