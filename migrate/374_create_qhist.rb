# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:qhist) do
      column :qh_id, :varchar, size: 10
      column :qh_quote_n, :varchar, size: 15
      column :qh_qq1, :integer
      column :qh_qq2, :integer
      column :qh_qq3, :integer
      column :qh_qq4, :integer
      column :qh_qq5, :integer
      column :qh_qq6, :integer
      column :qh_qq7, :integer
      column :qh_qq8, :integer
      column :qh_qq9, :integer
      column :qh_qq10, :integer
      column :qh_fcpu1, :float
      column :qh_fcpu2, :float
      column :qh_fcpu3, :float
      column :qh_fcpu4, :float
      column :qh_fcpu5, :float
      column :qh_fcpu6, :float
      column :qh_fcpu7, :float
      column :qh_fcpu8, :float
      column :qh_fcpu9, :float
      column :qh_fcpu10, :float
      column :qh_date, :date
      column :qh_user_id, :varchar, size: 5
      column :qh_note, :text
    end
  end
end
