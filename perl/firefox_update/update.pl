#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

my $NOW_VER = '3.6';
my $NEW_VER = '3.6.2';

my $local_file  = "/tmp/firefox-$NEW_VER.tar.bz2";
my $remote_file = "http://download.mozilla.org/?product=firefox-$NEW_VER&os=linux&lang=ja";
my $get_tbz2    = 'sudo wget -O '.$local_file. ' "'.$remote_file.'"';
warn $get_tbz2;
system($get_tbz2);

my $install_path = '/usr/lib/firefox';
my $rename_current_dir = "/usr/lib/firefox-$NOW_VER";
if(-e $install_path){
    my $backup_current_ver = "sudo mv $install_path $rename_current_dir";
    system($backup_current_ver);
}

my $untar_file = "sudo tar -jxvf $local_file -C /usr/lib/";
system($untar_file);

#my $set_icon = "sudo cp $rename_current_dir/icons/mozicon50.xpm $install_path/icons/";
#system($set_icon);

