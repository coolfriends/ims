# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:ns_nouns) do
      column :nn_noun, :varchar, size: 15
      column :nn_ns_code, :varchar, size: 5
    end
  end
end
