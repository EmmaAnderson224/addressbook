# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
cookbook_file "apt-sources.list" do
  path "/etc/apt/sources.list"
end
execute 'apt_update' do
  command 'apt-get update'
end

# Base configuration recipe in Chef.
package "wget"
package "ntp"
cookbook_file "ntp.conf" do
  path "/etc/ntp.conf"
end
execute 'ntp_restart' do
  command 'service ntp restart'
end


package "python3-pip"
execute 'install django' do
	command 'pip3 install django'
end


# run server to listen outside request
execute 'run_server' do
	
	cwd '/home/vagrant/project'
	command 'nohup python3 manage.py runserver 0:8000 2>/dev/null &'
end




