# frozen_string_literal: true

require 'json'
require 'sequel'
environment = ENV['IMS_ENV'] || 'test'
config = JSON.parse(File.read("config/ims-#{environment}.json"), symbolize_names: true)
DB = Sequel.postgres('ims', user: 'ims', password: config[:db_pass])
