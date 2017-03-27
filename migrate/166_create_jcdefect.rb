# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:jcdefect) do
      column :jd_id, :varchar, size: 10
      column :jd_jc_id, :varchar, size: 10
      column :jd_df_id, :varchar, size: 10
      column :jd_notes, :text
      column :jd_qty, :float
      column :jd_ship_co, :varchar, size: 18
      column :jd_aj_id, :varchar, size: 10
      column :jd_scrap, :float
      column :jd_rework, :float
      column :jd_review, :float
      column :jd_nd_id, :varchar, size: 10
    end
  end
end
