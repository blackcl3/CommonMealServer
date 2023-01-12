from commonmealapi.models import User
from commonmealapi.models import Neighborhood
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']
    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()
    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'id': user.id,
            'uid': user.uid,
            'name': user.name,
            'public_profile': user.public_profile,
            'photo_url': user.photo_url,
            'address': user.address,
            'neighborhood': user.neighborhood.id
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the commonmealapi_user table
    user = User.objects.create(
        name=request.data['name'],
        uid=request.data['uid'],
        public_profile=request.data['public_profile'],
        photo_url=request.data['photo_url'],
        address=request.data['address'],
        neighborhood=Neighborhood.objects.get(pk=request.data['neighborhood'])
    )

    # Return the user info to the client
    data = {
        'id': user.id,
        'uid': user.uid,
        'name': user.name,
        'public_profile': user.public_profile,
        'photo_url': user.photo_url,
        'address': user.address,
        'neighborhood': user.neighborhood.id
    }
    return Response(data)
