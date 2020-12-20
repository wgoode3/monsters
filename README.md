# Monsters

This is an example repo for learning about Django REST!

### Getting Started

After cloning the repo, `cd` into the main project and create a virtual environment

```sh
cd monsters
python3 -m venv RESTenv
source RESTenv/bin/activate # On Windows use `RESTenv\Scripts\activate`
pip install -r requirements.txt
python3 manage.py runserver
```

Then when we navigate to `http://localhost:8000/api/monsters` we will see the list of our monsters as well as a form to create new monsters.

If we want to examine a monster in detail we should add an `id` to the end of the url... like `http://localhost:8000/api/monsters2`

This should give us back a page with something like:

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "name": "Werewolf",
    "height": 2.0,
    "description": "Is a very hairy individual. Loves the moon!\r\n\r\nAWOOO~",
    "created_at": "2020-12-20T10:43:31.251376Z",
    "updated_at": "2020-12-20T10:43:31.251415Z"
}
```

We can also make `PUT` and `DELETE` requests from this page

### Consuming the data as JSON

If we want to get back the raw data for use with our own front-end, we need to add on the `format` query parameter.

For instance if we're using `axios` we can make a request like...

```js
axios.get("http://localhost:8000/api/monsters?format=json").
    then(res => {
        // TODO - handle data in the response however we like
        console.log("The response coming from the monster rest api\n", res);
    }).catch(err => console.error(err));
```

### COMING SOON - Authenticating requests!