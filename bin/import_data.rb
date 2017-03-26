require 'pry'
require 'dbf'
require 'sequel'
require 'json'
config = JSON.parse(File.read('config/test.json'), :symbolize_names => true)

tables = ARGV
tables = Dir['data/*.dbf'] unless tables.size > 0
DB = Sequel.postgres('ims', user: 'ims', password: config[:db_pass])

def fix_hash(h)
  h["or_loctime"] = nil
end

tables.each do |table|
  table_name = File.basename(table).split('.').first
  dbf = DBF::Table.new(table)
  rows = 1
  dbf.each do |row|
    puts "Loading row #{rows} of table #{table_name}"
    rows += 1
    row_hash = Hash[row.attributes.map { |k,v| [k.downcase, v] }]
    tries = 0
    begin
      DB[table_name.to_sym].insert row_hash
    rescue
      fix_hash row_hash
      tries += 1
      retry if tries< 2
      stdout.puts $!
      binding.pry
    end
  end
end
