# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:po_rectc) do
      column :pt_po_num, :varchar, size: 7
      column :pt_line_nu, :integer
      column :pt_rec_num, :integer
      column :pt_date, :date
      column :pt_userid, :varchar, size: 5
      column :pt_startti, DateTime
      column :pt_endtime, DateTime
      column :pt_timeela, :float
      column :pt_pr_rec_, :integer
      column :pt_id, :integer
    end
  end
end
