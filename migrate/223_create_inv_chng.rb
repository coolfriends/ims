# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:inv_chng) do
      column :iy_id, :varchar, size: 10
      column :iy_invent_, :varchar, size: 30
      column :iy_year, :varchar, size: 4
      column :iy_month_1, :float
      column :iy_month_2, :float
      column :iy_month_3, :float
      column :iy_month_4, :float
      column :iy_month_5, :float
      column :iy_month_6, :float
      column :iy_month_7, :float
      column :iy_month_8, :float
      column :iy_month_9, :float
      column :iy_month10, :float
      column :iy_month11, :float
      column :iy_month12, :float
      column :iy_quantit, :float
      column :iy_quanti2, :float
      column :iy_quanti3, :float
      column :iy_quanti4, :float
      column :iy_quanti5, :float
      column :iy_quanti6, :float
      column :iy_quanti7, :float
      column :iy_quanti8, :float
      column :iy_quanti9, :float
      column :iy_quant10, :float
      column :iy_quant11, :float
      column :iy_quant12, :float
    end
  end
end
