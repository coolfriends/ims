# frozen_string_literal: true

require 'pry'
require 'dbf'
require 'sequel'
require 'json'
require_relative '../db/init'

tables = ARGV
tables = Dir['data/*.dbf'] if tables.empty?

def fix_hash(h)
  h['or_loctime'] = nil if h.key? 'or_loctime'
  h['sd_last_mo'] = nil if h.key? 'sd_last_mo'
end

tables.each do |table|
  table_name = File.basename(table).split('.').first
  dbf = DBF::Table.new(table)
  rows = 1
  dbf.each do |row|
    puts "Loading row #{rows} of table #{table_name}"
    rows += 1
    row_hash = Hash[row.attributes.map { |k, v| [k.downcase, v] }]
    tries = 0
    begin
      DB[table_name.to_sym].insert row_hash
    rescue
      fix_hash row_hash
      tries += 1
      retry if tries < 2
      $stderr.puts $ERROR_INFO
      binding.pry # rubocop:disable Lint/Debugger
    end
  end
end
