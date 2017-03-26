require 'dbf'
require 'pry'
count = 1
Dir['data/*.dbf'].each do |table|
  migration = File.join("migrate", "%03d" % count)
  count += 1
  table_name = File.basename(table).split('.').first
  migration_name = "#{migration}_create_#{table_name}.rb"
  puts "Creating #{migration_name}"
  binding.pry if $DEBUG
  `dbf -r #{table} > #{migration_name}`
end
