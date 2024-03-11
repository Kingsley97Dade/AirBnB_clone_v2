# 101-setup_web_static.pp
# This Puppet manifest configures a web server for the deployment of web_static.

class web_static {
  # Install Nginx if not installed
  package { 'nginx':
    ensure => installed,
  }

  # Create necessary directories
  file { '/data':
    ensure => directory,
  }

  file { '/data/web_static':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/shared':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Create a fake HTML file
  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => '<html><head></head><body>Test Page</body></html>',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  # Create or recreate symbolic link
  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    force  => true,
  }

  # Update Nginx configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('web_static/nginx_config.erb'),
    notify  => Service['nginx'],
  }

  # Restart Nginx
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

include web_static

