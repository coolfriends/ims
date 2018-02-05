#!/usr/bin/env ruby
# frozen_string_literal: true

require 'dbf'
require 'pry'

# Remove migrate dir if it exists, then create empty migrate dir
directory = 'migrate'
FileUtils.remove_dir directory if File.directory? directory
Dir.mkdir directory

# Make migrations happen
count = 1
Dir['data/*.dbf'].each do |table|
  migration = File.join('migrate', format('%03d', count))
  count += 1
  table_name = File.basename(table).split('.').first
  migration_name = "#{migration}_create_#{table_name}.rb"
  puts "Creating #{migration_name}"
  binding.pry if $DEBUG # rubocop:disable Lint/Debugger
  `dbf -r #{table} > #{migration_name}`
end
