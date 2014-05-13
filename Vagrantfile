VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos6"
  config.vm.box_url = "https://s3.amazonaws.com/itmat-public/centos-6.3-chef-10.14.2.box"

  config.vm.define "gw" do |gw|
    gw.vm.network "private_network", ip: "192.168.111.222"

    gw.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/provisioning/gw.yml"
    end
  end

  config.vm.define "web" do |web|
    web.vm.network "private_network", ip: "192.168.111.223"
  end
end
