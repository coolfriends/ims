require 'json'
require 'sequel'
config = JSON.parse(File.read('config/test.json'), symbolize_names: true)
DB = Sequel.postgres('ims', user: 'ims', password: config[:db_pass])
