#!/usr/bin/perl -w

use strict;
use warnings;

select STDOUT; $| = 1;

while (<>) {
    my @parts = split;
    my $url = $parts[0];

    if ($url =~ /celuit\.edu\.vn\/.*\.(png|jpg|jpeg|gif|bmp|svg)(\?.*)?$/i) {
        print "http://10.0.3.4/sign.jpeg\n";
    } else {
        print "\n";
    }
}s