/* eslint-disable no-underscore-dangle */
/* eslint-disable no-return-assign */
import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    // eslint-disable-next-line no-underscore-dangle
    this._floors = floors;
  }

  get sqft() {
    return super.sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    return super.sqft = newSqft;
  }

  get floors() {
    return this._floors;
  }

  set floors(newFloors) {
    if (typeof newFloors !== 'number') {
      throw new TypeError('floors must be a number');
    }
    return this._floors = newFloors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
