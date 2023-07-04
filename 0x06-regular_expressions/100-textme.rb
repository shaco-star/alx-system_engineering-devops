#!/usr/bin/env ruby
format = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)
list = format.map { |match| match.compact.first }
puts list.join(',')
