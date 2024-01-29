/* eslint-disable */
import signUpUser from "./4-user-promise.js";
import uploadPhoto from "./5-photo-reject.js";

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((values) => {
      for (const value of values) {
        if (value.status === "rejected") {
          value.value = `Error: ${value.reason.message}`;
          delete value.reason;
        }
      }
      return values;
    });
}
