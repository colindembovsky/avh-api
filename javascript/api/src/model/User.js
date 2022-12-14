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
 * The User model module.
 * @module model/User
 * @version 1.0.3
 */
class User {
    /**
     * Constructs a new <code>User</code>.
     * /_**
     * @alias module:model/User
     * @param id {String} User ID
     * @param label {String} User Label
     * @param name {String} User Name
     * @param email {String} User Email
     */
    constructor(id, label, name, email) { 
        
        User.initialize(this, id, label, name, email);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, label, name, email) { 
        obj['id'] = id;
        obj['label'] = label;
        obj['name'] = name;
        obj['email'] = email;
    }

    /**
     * Constructs a <code>User</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/User} obj Optional instance to populate.
     * @return {module:model/User} The populated <code>User</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new User();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('administrator')) {
                obj['administrator'] = ApiClient.convertToType(data['administrator'], 'Boolean');
            }
        }
        return obj;
    }


}

/**
 * User ID
 * @member {String} id
 */
User.prototype['id'] = undefined;

/**
 * User Label
 * @member {String} label
 */
User.prototype['label'] = undefined;

/**
 * User Name
 * @member {String} name
 */
User.prototype['name'] = undefined;

/**
 * User Email
 * @member {String} email
 */
User.prototype['email'] = undefined;

/**
 * the flag that specifies whether user is Administrator or not
 * @member {Boolean} administrator
 */
User.prototype['administrator'] = undefined;






export default User;

