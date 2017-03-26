Sequel.migration do
  change do
     create_table(:gagetype) do
      column :gt_code, :varchar, :size => 10
      column :gt_desc, :varchar, :size => 40
      column :gt_toleran, :float
      column :gt_interva, :float
      column :gt_interv2, :float
      column :gt_interv3, :float
      column :gt_interv4, :float
      column :gt_interv5, :float
      column :gt_note, :text
      column :gt_blk_siz, :float
      column :gt_blk_si2, :float
      column :gt_range, :varchar, :size => 30
      column :gt_interv6, :float
      column :gt_interv7, :float
      column :gt_paralle, :float
      column :gt_cylindr, :float
    end
  end
end
