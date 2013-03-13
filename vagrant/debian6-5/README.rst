
Please fix authorized_keys link if $HOME/.ssh/authorized_keys does NOT exist.

setup
---------------------------

.. code-block:: none
  
  # vagrant setup
  vagrant up
  vagrant gem install sahara
  cd chef-repo
  # chef install @ node
  knife solo prepare root@192.168.99.15
  # exec cookbook @ node
  knife solo cook root@192.168.99.15

