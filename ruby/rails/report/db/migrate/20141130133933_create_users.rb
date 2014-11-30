class CreateUsers < ActiveRecord::Migration
  def change
    create_table :users do |t|
      t.string :name
      t.integer :account_id
      t.integer :status

      t.timestamps
    end
  end
end
