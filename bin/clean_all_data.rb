#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../db/init'
DB.tables.each do |table|
  DB[table].delete
end
