Vagrant.configure("2") do |config|
    servers=[
        {
            :hostname => "workstation",
            :box => "bento/ubuntu-22.04",
            :ip => "192.168.56.15",
            :ssh_port => "2200"
        },
        {
            :hostname => "jenkins-controller",
            :box => "bento/ubuntu-22.04",
            :ip => "192.168.56.16",
            :ssh_port => "2201"
        },
        {
            :hostname => "jenkins-agent",
            :box => "bento/ubuntu-22.04",
            :ip => "192.168.56.17",
            :ssh_port => "2205"
        }    
    ]

    servers.each do |machine|
        config.vm.box_check_update = false
        config.vm.define machine[:hostname] do |server|
            server.vm.box = machine[:box]
            server.vm.hostname = machine[:hostname]
            server.vm.network :private_network, ip: machine[:ip]
            server.vm.network "forwarded_port", guest: 22, host: machine[:ssh_port], id: "ssh"
            server.ssh.forward_agent = true
            server.vm.provider :virtualbox do |vb|
                vb.customize ["modifyvm", :id, "--memory", 1024]
                vb.customize ["modifyvm", :id, "--cpus", 1]
                vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
            end
        end
    end
end






