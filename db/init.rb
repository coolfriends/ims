# frozen_string_literal: true

require 'json'
require 'sequel'
environment = ENV['IMS_ENV'] || 'test'
config = JSON.parse(File.read("config/ims-#{environment}.json"),
                    symbolize_names: true)
DB = Sequel.connect("postgres://ims:#{config[:db_pass]}@localhost/ims")
