Sequel.migration do
  change do
     create_table(:ac_clinc) do
      column :ci_id, :varchar, :size => 10
      column :ci_cust_co, :varchar, :size => 6
      column :ci_user_id, :varchar, :size => 5
      column :ci_date, :date
      column :ci_type, :varchar, :size => 1
      column :ci_status, :varchar, :size => 1
      column :ci_inv_num, :varchar, :size => 7
      column :ci_cc_id, :varchar, :size => 10
      column :ci_contact, :varchar, :size => 25
      column :ci_promise, :date
      column :ci_notes, :text
      column :ci_cn_leve, :integer
    end
  end
end
