import boto3
from datetime import datetime, timezone
import json
import os
import uuid


def lambda_handler(event, context):
    body = event['body']
    jsonBody = json.loads(body)
    uniqueId = uuid.uuid4().hex
    dateTimeString = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
    itemForDb = {}
    itemForDb['activityId'] = dateTimeString + '-' + uniqueId
    itemForDb['dateTime'] = dateTimeString

    if 'activityType' in jsonBody:
        activityType = jsonBody['activityType']
        itemForDb['activityType'] = activityType
    if 'autoPlay_AutoAdvanceLesson' in jsonBody:
        autoPlay_AutoAdvanceLesson = jsonBody['autoPlay_AutoAdvanceLesson']
        itemForDb['autoPlay_AutoAdvanceLesson'] = autoPlay_AutoAdvanceLesson
    if 'chunkIndex' in jsonBody:
        chunkIndex = jsonBody['chunkIndex']
        itemForDb['chunkIndex'] = chunkIndex
    if 'chunkIndex_New' in jsonBody:
        chunkIndex_New = jsonBody['chunkIndex_New']
        itemForDb['chunkIndex_New'] = chunkIndex_New
    if 'chunkIndex_Previous' in jsonBody:
        chunkIndex_Previous = jsonBody['chunkIndex_Previous']
        itemForDb['chunkIndex_Previous'] = chunkIndex_Previous
    if 'iKnowThis_AllChunksInLessonSuppressed' in jsonBody:
        iKnowThis_AllChunksInLessonSuppressed = jsonBody['iKnowThis_AllChunksInLessonSuppressed']
        itemForDb['iKnowThis_AllChunksInLessonSuppressed'] = iKnowThis_AllChunksInLessonSuppressed
    if 'learningModeDisplayName' in jsonBody:
        learningModeDisplayName = jsonBody['learningModeDisplayName']
        itemForDb['learningModeDisplayName'] = learningModeDisplayName
    if 'learningModeDisplayName_New' in jsonBody:
        learningModeDisplayName_New = jsonBody['learningModeDisplayName_New']
        itemForDb['learningModeDisplayName_New'] = learningModeDisplayName_New
    if 'learningModeDisplayName_Previous' in jsonBody:
        learningModeDisplayName_Previous = jsonBody['learningModeDisplayName_Previous']
        itemForDb['learningModeDisplayName_Previous'] = learningModeDisplayName_Previous
    if 'lessonId' in jsonBody:
        lessonId = jsonBody['lessonId']
        itemForDb['lessonId'] = lessonId
    if 'lessonId_New' in jsonBody:
        lessonId_New = jsonBody['lessonId_New']
        itemForDb['lessonId_New'] = lessonId_New
    if 'lessonId_Previous' in jsonBody:
        lessonId_Previous = jsonBody['lessonId_Previous']
        itemForDb['lessonId_Previous'] = lessonId_Previous
    if 'lessonName_NativeLanguage' in jsonBody:
        lessonName_NativeLanguage = jsonBody['lessonName_NativeLanguage']
        itemForDb['lessonName_NativeLanguage'] = lessonName_NativeLanguage
    if 'lessonName_NativeLanguage_New' in jsonBody:
        lessonName_NativeLanguage_New = jsonBody['lessonName_NativeLanguage_New']
        itemForDb['lessonName_NativeLanguage_New'] = lessonName_NativeLanguage_New
    if 'lessonName_NativeLanguage_Previous' in jsonBody:
        lessonName_NativeLanguage_Previous = jsonBody['lessonName_NativeLanguage_Previous']
        itemForDb['lessonName_NativeLanguage_Previous'] = lessonName_NativeLanguage_Previous
    if 'lessonProviderId' in jsonBody:
        lessonProviderId = jsonBody['lessonProviderId']
        itemForDb['lessonProviderId'] = lessonProviderId
    if 'lessonProviderId_New' in jsonBody:
        lessonProviderId_New = jsonBody['lessonProviderId_New']
        itemForDb['lessonProviderId_New'] = lessonProviderId_New
    if 'lessonProviderId_Previous' in jsonBody:
        lessonProviderId_Previous = jsonBody['lessonProviderId_Previous']
        itemForDb['lessonProviderId_Previous'] = lessonProviderId_Previous
    if 'lessonVersion' in jsonBody:
        lessonVersion = jsonBody['lessonVersion']
        itemForDb['lessonVersion'] = lessonVersion
    if 'lessonVersion_New' in jsonBody:
        lessonVersion_New = jsonBody['lessonVersion_New']
        itemForDb['lessonVersion_New'] = lessonVersion_New
    if 'lessonVersion_Previous' in jsonBody:
        lessonVersion_Previous = jsonBody['lessonVersion_Previous']
        itemForDb['lessonVersion_Previous'] = lessonVersion_Previous
    if 'project' in jsonBody:
        project = jsonBody['project']
        itemForDb['project'] = project
    if 'userDepartment' in jsonBody:
        userDepartment = jsonBody['userDepartment']
        itemForDb['userDepartment'] = userDepartment
    if 'userGroup' in jsonBody:
        userGroup = jsonBody['userGroup']
        itemForDb['userGroup'] = userGroup
    if 'userFirstName' in jsonBody:
        userFirstName = jsonBody['userFirstName']
        itemForDb['userFirstName'] = userFirstName
    if 'userLastName' in jsonBody:
        userLastName = jsonBody['userLastName']
        itemForDb['userLastName'] = userLastName
    if 'userOrganization' in jsonBody:
        userOrganization = jsonBody['userOrganization']
        itemForDb['userOrganization'] = userOrganization
    if 'userSubgroup' in jsonBody:
        userSubgroup = jsonBody['userSubgroup']
        itemForDb['userSubgroup'] = userSubgroup

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ.get('TABLE_NAME'))
    table.put_item(
        Item=itemForDb
    )

    return {
        'statusCode': 200
    }

















