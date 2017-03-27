# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:trucktyp) do
      column :tt_id, :varchar, size: 10
      column :tt_desc, :varchar, size: 40
      column :tt_ext_des, :text
      column :tt_maxwgt, :float
      column :tt_axles, :integer
      column :tt_length, :float
      column :tt_width, :float
      column :tt_height, :float
    end
  end
end
