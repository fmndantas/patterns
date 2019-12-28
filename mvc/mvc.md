# Model-view-controller pattern

* It is a compound pattern (more than one pattern working together
to achieve an goal).

* Used mainly to implement **user interfaces**.

* Model
    * represents the data and business logic
    * implements
        * data creation
        * data modification
        * data removal
    
* View
    * how the data is presented
    * GUI
    * **should not** contain any logic
    
* Controller
    * sets the model and view behaviours, based on what the user needs.
 
# Usage cases

* To decouple presentation from business logic
* To use multiple controllers to change the representation
* Flexibility between the three components (model, view, controller)

# Model

* The autonomous part of application
* Does not control how data is presented to the client
* Controller and view are depend on the model

# View

* Sets the way how client sees data
* **SHOULD NOT** contain any business logic
* It should avoids to interact directly with database. Instead,
the existing models should be used to get data from database.

# Controller

* Glue between the model and view
* Controls the interaction of the user on the interface
* Passes the data from the model to the view
* It **SHOULD NOT** make database calls or get involved with presentation.
* It should be as thin as possible.