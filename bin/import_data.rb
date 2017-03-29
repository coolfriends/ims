#!/usr/bin/env ruby
# frozen_string_literal: true

require 'pry'
require 'dbf'
require 'sequel'
require 'json'
require_relative '../db/init'

tables = ARGV
tables = Dir['data/*.dbf'].sort { |a, b| File.basename(a) <=> File.basename(b) } if tables.empty? # rubocop:disable Metrics/LineLength

def fix_hash(h) # rubocop:disable Metrics/MethodLength
  %w(me_timetor
     mr_lm_date
     em_lm_date
     mr_when_re
     mr_deadlin
     iu_transti
     iv_last_mo
     io_act_dat
     mn_lm_date
     gj_last_mo
     in_lm_date
     cc_call_cy
     cc_last_up
     ao_infsta2
     ap_lm_date
     ao_infend2
     ij_last_mo
     or_loctime
     sd_last_mo).each do |key|
    h[key] = nil if h.key? key
  end
  %w(cc_email1d
     w3_501c_n2
     w3_501c_sl
     cc_email2d
     em_1099box
     em_w2_3rd_
     use_1x2_bi
     sc_2nd_tin
     mn_1099box
     w3_501c_no
     sc_409a_de
     w2_3rd_sic
     sc_409a_in
     ca_2d_barc
     cc_email3d).each do |key|
    if h.key? key
      h[key.sub(/(\d)(\w)$/, '\1_\2')] = h[key]
      h.delete(key)
    end
  end
end

tables.each do |table|
  table_name = File.basename(table).split('.').first
  dbf = DBF::Table.new(table)
  rows = 1
  dbf.each do |row|
    puts "Loading row #{rows} of table #{table_name}" if (rows % 100).zero?
    rows += 1
    next if row.nil?
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
