/**
 * Arm API
 *    This documents the Arm Virtual Hosting REST API.  For other examples and API clients such as python or javascript please see [API Clients (python/javascript)](https://github.com/ARM-software/avh-api).   For a guide on using this interface please see [API Quickstart](https://intercom.help/arm-avh/en/articles/6134791-quickstart-for-the-api-docs)   ## Links   - [API Quickstart](https://intercom.help/arm-avh/en/articles/6134791-quickstart-for-the-api-docs)   - [API Clients (python/javascript)](https://github.com/arm-software/avh-api)   
 *
 * The version of the OpenAPI document: 3.15.0-15704
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Trial model module.
 * @module model/Trial
 * @version 1.0.3
 */
class Trial {
    /**
     * Constructs a new <code>Trial</code>.
     * Trial options
     * @alias module:model/Trial
     * @param duration {Number} Duration in days
     */
    constructor(duration) { 
        
        Trial.initialize(this, duration);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, duration) { 
        obj['duration'] = duration;
    }

    /**
     * Constructs a <code>Trial</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Trial} obj Optional instance to populate.
     * @return {module:model/Trial} The populated <code>Trial</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Trial();

            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'Number');
            }
        }
        return obj;
    }


}

/**
 * Duration in days
 * @member {Number} duration
 */
Trial.prototype['duration'] = undefined;






export default Trial;

