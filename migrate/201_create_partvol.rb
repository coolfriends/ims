# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:partvol) do
      column :pv_id, :integer
      column :invent_num, :varchar, size: 30
      column :invent_des, :varchar, size: 50
      column :cust_code, :varchar, size: 6
      column :numsu52, :integer
      column :numsuem, :integer
      column :numsuq, :integer
      column :year1, :integer
      column :year2, :integer
      column :year3, :integer
      column :year4, :integer
      column :last52, :integer
      column :last26, :integer
      column :last13, :integer
      column :last5, :integer
      column :week1, :integer
      column :week2, :integer
      column :week3, :integer
      column :week4, :integer
      column :week5, :integer
      column :next5, :integer
      column :lastvsnext, :integer
      column :ofi, :float
      column :shipped52, :integer
      column :shippedem, :integer
      column :shippedq, :integer
      column :month1, :integer
      column :month2, :integer
      column :month3, :integer
      column :month4, :integer
      column :month5, :integer
      column :month6, :integer
      column :month7, :integer
      column :month8, :integer
      column :month9, :integer
      column :month10, :integer
      column :month11, :integer
      column :month12, :integer
    end
  end
end
