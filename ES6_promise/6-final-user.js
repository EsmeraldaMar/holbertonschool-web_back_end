import signUpUser from './4-user-promise';
import { uploadPhoto } from './5-photo-reject';

export default function (firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName)
    .then((value) => ({ status: 'fulfilled', value }))
    .catch((error) => ({ status: 'rejected', value: `${error.message}` }));

  const photoPromise = uploadPhoto(fileName)
    .then((value) => ({ status: 'fulfilled', value }))
    .catch((error) => ({ status: 'rejected', value: `${error.message}` }));

  return Promise.all([userPromise, photoPromise]);
}
