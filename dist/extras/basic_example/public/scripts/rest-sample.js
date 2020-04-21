// Copyright (C) <2018> Intel Corporation
//
// SPDX-License-Identifier: Apache-2.0

// REST samples. It sends HTTP requests to sample server, and sample server sends requests to conference server.
// Both this file and sample server are samples.
'use strict';
var send = function (method, path, body, onRes, host) {
    var req = new XMLHttpRequest()
    req.onreadystatechange = function () {
        if (req.readyState === 4) {
            onRes(req.responseText);
        }
    };
    let url = generateUrl(host, path);
    req.open(method, url, true);
    req.setRequestHeader('Content-Type', 'application/json');
    if (body !== undefined) {
        req.send(JSON.stringify(body));
    } else {
        req.send();
    }
};

var generateUrl = function(host, path) {
    let url;
    if (host !== undefined) {
        url = host + path;  // Use the host user set.
    }else {
        let u = new URL(document.URL);
        url = u.origin + path;  // Get the string before last '/'.
    }
    return url;
}

var onResponse = function (result) {
    if (result) {
        try {
            console.info('Result:', JSON.parse(result));
        } catch (e) {
            console.info('Result:', result);
        }
    } else {
        console.info('Null');
    }
};

var mixStream = function (room, stream, view, host) {
    var jsonPatch = [{
        op: 'add',
        path: '/info/inViews',
        value: view
    }];
    console.info('mixStream:', stream);
    send('PATCH', '/rooms/' + room + '/streams/' + stream, jsonPatch,
        onResponse, host);
};

var startStreamingIn = function (room, inUrl, host) {
    var options = {
        url: inUrl,
        media: {
            audio: 'auto',
            video: true
        },
        transport: {
            protocol: 'udp',
            bufferSize: 2048
        }
    };
    send('POST', '/rooms/' + room + '/streaming-ins', options, onResponse, host);
};

var startStreamingOut = function (room, stream, outUrl, host) {
    var options = {
        protocol: 'rtmp',
        url: outUrl,
        parameters:{
        },
        media: {
            audio: {
                from: stream
            },
            video: {
                from: stream
            }
        }
    };
    console.info('startStreamingOut:', stream);
    send('POST', '/rooms/' + room + '/streaming-outs', options, onResponse, host);
};

var createToken = function (room, user, role, callback, host) {
    var body = {
        room: room,
        user: user,
        role: role
    };
    send('POST', '/tokens/', body, callback, host);
};

var getRoom = function (room,callback, host) {
    send('GET', '/rooms/'+ room,undefined, callback, host);
};

var updateRoom = function (room,roomInfo, host) {
    send('PUT', '/rooms/'+ room,roomInfo, onResponse, host);
};

// var updateRoomResolution = function (room, host) {
    // var options={
    //     publishLimit: -1,
    //     userLimit: -1,
    //     enableMixing: 1,
    //     viewports: [
    //       {
    //         name: "common",
    //         mediaMixing: {
    //           video: {
    //             maxInput: 15,
    //             resolution: 'hd720p',
    //             quality_level: 'standard',
    //             bkColor: {"r":1, "g":2, "b":255},
    //             layout: {
    //               base: 'lecture',
    //             },
    //             avCoordinated: 1,
    //             crop: 1
    //           },
    //           audio: null
    //         },
    //       }
    //     ]
    //   };
//     send('PUT', '/rooms/'+ room,options, onResponse, host);
// };