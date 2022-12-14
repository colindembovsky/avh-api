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
 * The KernelThread model module.
 * @module model/KernelThread
 * @version 1.0.3
 */
class KernelThread {
    /**
     * Constructs a new <code>KernelThread</code>.
     * 
     * @alias module:model/KernelThread
     */
    constructor() { 
        
        KernelThread.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>KernelThread</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/KernelThread} obj Optional instance to populate.
     * @return {module:model/KernelThread} The populated <code>KernelThread</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new KernelThread();

            if (data.hasOwnProperty('kernelId')) {
                obj['kernelId'] = ApiClient.convertToType(data['kernelId'], 'String');
            }
            if (data.hasOwnProperty('tid')) {
                obj['tid'] = ApiClient.convertToType(data['tid'], 'Number');
            }
            if (data.hasOwnProperty('stack')) {
                obj['stack'] = ApiClient.convertToType(data['stack'], ['String']);
            }
        }
        return obj;
    }


}

/**
 * Kernel Thread ID
 * @member {String} kernelId
 */
KernelThread.prototype['kernelId'] = undefined;

/**
 * Task ID
 * @member {Number} tid
 */
KernelThread.prototype['tid'] = undefined;

/**
 * Array of stack addresses
 * @member {Array.<String>} stack
 */
KernelThread.prototype['stack'] = undefined;






export default KernelThread;

