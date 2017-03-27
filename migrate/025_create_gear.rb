# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:gear) do
      column :gr_id, :varchar, size: 10
      column :gr_schgrp, :varchar, size: 10
      column :gr_type, :varchar, size: 1
      column :gr_driver, :integer
      column :gr_driven, :integer
      column :gr_rpm, :integer
      column :gr_mds_rpm, :integer
    end
  end
end
